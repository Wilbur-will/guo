import json
import sqlite3

from app.paths import DB_PATH, SEED_DATA_PATH
import main  # noqa: F401 - importing main creates the database schema


def insert_seed_data():
    if not SEED_DATA_PATH.exists():
        print(f"No seed data found at {SEED_DATA_PATH}")
        return

    with SEED_DATA_PATH.open("r", encoding="utf-8") as seed_file:
        seed_data = json.load(seed_file)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    demo_password = seed_data.get("demo_password", "123456")

    for user in seed_data.get("users", []):
        username = user.get("username")
        if not username:
            continue
        cursor.execute(
            """
            INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET avatar = excluded.avatar
            """,
            (username, demo_password, user.get("avatar")),
        )

    for post in seed_data.get("posts", []):
        cursor.execute(
            """
            INSERT OR IGNORE INTO posts
            (id, title, content, photos, location, latitude, longitude, duration, people,
             author, publish_time, likes, comments, views, city, audio_url, audio_url_en,
             guide_items, route_map, tags, heritage_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                post.get("id"),
                post.get("title"),
                post.get("content", ""),
                post.get("photos"),
                post.get("location"),
                post.get("latitude"),
                post.get("longitude"),
                post.get("duration"),
                post.get("people"),
                post.get("author"),
                post.get("publish_time"),
                post.get("likes", 0),
                post.get("comments", 0),
                post.get("views", 0),
                post.get("city", ""),
                post.get("audio_url", ""),
                post.get("audio_url_en", ""),
                post.get("guide_items", "[]"),
                post.get("route_map", "{}"),
                post.get("tags", "[]"),
                post.get("heritage_id"),
            ),
        )

    for follow in seed_data.get("follows", []):
        cursor.execute(
            "INSERT OR IGNORE INTO follows (follower, following) VALUES (?, ?)",
            (follow.get("follower"), follow.get("following")),
        )

    for comment in seed_data.get("comments", []):
        cursor.execute(
            """
            INSERT OR IGNORE INTO comments (id, post_id, author, content, publish_time)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                comment.get("id"),
                comment.get("post_id"),
                comment.get("author"),
                comment.get("content"),
                comment.get("publish_time"),
            ),
        )

    for favorite in seed_data.get("favorites", []):
        cursor.execute(
            "INSERT OR IGNORE INTO favorites (username, post_id) VALUES (?, ?)",
            (favorite.get("username"), favorite.get("post_id")),
        )

    for like in seed_data.get("post_likes", []):
        cursor.execute(
            "INSERT OR IGNORE INTO post_likes (username, post_id) VALUES (?, ?)",
            (like.get("username"), like.get("post_id")),
        )

    conn.commit()
    conn.close()
    print(f"Seeded {len(seed_data.get('posts', []))} posts into {DB_PATH}")


if __name__ == "__main__":
    insert_seed_data()
