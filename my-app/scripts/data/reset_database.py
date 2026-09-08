import sqlite3
import sys
from pathlib import Path

BOOTSTRAP_ROOT = Path(__file__).resolve().parents[2]
if str(BOOTSTRAP_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOTSTRAP_ROOT))

from app.paths import DB_PATH

TEST_USERS = ['travel_boy', 'beijing_fan', 'explorer', 'nature_lover', 'culture_seeker']

def reset_database(keep_test_data=True):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # 先关闭外键约束
    c.execute('PRAGMA foreign_keys = OFF')
    c.execute('''CREATE TABLE IF NOT EXISTS post_likes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        UNIQUE(username, post_id)
    )''')
    
    if keep_test_data:
        # 只删除非测试用户的数据
        # 先获取所有非测试用户的帖子ID
        c.execute('''
            SELECT p.id FROM posts p 
            WHERE p.author NOT IN ({})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)
        post_ids = [row[0] for row in c.fetchall()]
        
        if post_ids:
            placeholders = ','.join(['?']*len(post_ids))
            
            # 删除相关评论
            c.execute(f'DELETE FROM comments WHERE post_id IN ({placeholders})', post_ids)
            
            # 删除相关收藏
            c.execute(f'DELETE FROM favorites WHERE post_id IN ({placeholders})', post_ids)

            # 删除相关点赞
            c.execute(f'DELETE FROM post_likes WHERE post_id IN ({placeholders})', post_ids)
            
            # 删除非测试用户的帖子
            c.execute('''
                DELETE FROM posts WHERE author NOT IN ({})
            '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)
        
        # 删除非测试用户之间的关注
        c.execute('''
            DELETE FROM follows 
            WHERE follower NOT IN ({0}) OR following NOT IN ({0})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS * 2)
        
        # 删除非测试用户的收藏
        c.execute('''
            DELETE FROM favorites WHERE username NOT IN ({})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)

        # 删除非测试用户的点赞
        c.execute('''
            DELETE FROM post_likes WHERE username NOT IN ({})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)
        
        # 删除非测试用户的消息
        c.execute('''
            DELETE FROM messages 
            WHERE sender NOT IN ({0}) OR receiver NOT IN ({0})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS * 2)
        
        # 删除非测试用户的评论
        c.execute('''
            DELETE FROM comments WHERE author NOT IN ({})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)
        
        # 删除非测试用户
        c.execute('''
            DELETE FROM users WHERE username NOT IN ({})
        '''.format(','.join(['?']*len(TEST_USERS))), TEST_USERS)
        
        print('✅ 已删除所有用户自主上传的内容，保留测试数据！')
        
    else:
        # 清空所有表
        tables = [
            'messages',
            'favorites',
            'post_likes',
            'follows',
            'comments',
            'posts',
            'users'
        ]
        
        for table in tables:
            c.execute(f'DELETE FROM {table}')
            print(f'已清空表: {table}')
        
        print('✅ 数据库已完全清空！')
    
    # 重置自增ID（只重置有数据删除的表）
    c.execute("DELETE FROM sqlite_sequence WHERE name IN ('users', 'posts', 'comments', 'follows', 'favorites', 'post_likes', 'messages')")
    
    # 重新开启外键约束
    c.execute('PRAGMA foreign_keys = ON')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print('请选择重置方式：')
    print('1. 只删除用户自主上传的内容（保留测试数据）')
    print('2. 完全清空所有数据')
    
    choice = input('\n请输入选项 (1 或 2): ')
    
    if choice == '1':
        reset_database(keep_test_data=True)
    elif choice == '2':
        confirm = input('⚠️  警告：这将删除所有数据！确定要继续吗？(yes/no): ')
        if confirm.lower() == 'yes' or confirm.lower() == 'y':
            reset_database(keep_test_data=False)
        else:
            print('已取消操作。')
    else:
        print('无效选项，已取消。')
