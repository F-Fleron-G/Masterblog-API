from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Get all blog posts in a simple JSON list.
    Friendly reminder: this just returns all current posts.
    """
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def create_post():
    """
    Create a new blog post.
    Send a JSON body with 'title' and 'content' to add it to our list.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid request. JSON data is required."}), 400

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        missing_fields = []
        if not title:
            missing_fields.append("title")
        if not content:
            missing_fields.append("content")
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    new_id = max((post["id"] for post in POSTS), default=0) + 1

    new_post = {
        "id": new_id,
        "title": title,
        "content": content
    }

    POSTS.append(new_post)

    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    Delete a blog post by its ID.
    If found, the post is removed and a success message is returned.
    Otherwise, a 404 error is returned.
    """
    for i, post in enumerate(POSTS):
        if post['id'] == post_id:
            del POSTS[i]
            return jsonify({
                "message": f"Post with id {post_id} has been deleted successfully."
            }), 200

    return jsonify({"error": "Post not found"}), 404


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """
    Update an existing blog post by its ID.
    Provide 'title' and/or 'content' in JSON to change the post.
    If not found, returns a 404 error.
    """
    data = request.get_json()
    if data is None:
        data = {}

    title = data.get("title", None)
    content = data.get("content", None)

    for post in POSTS:
        if post["id"] == post_id:
            if title is not None:
                post["title"] = title
            if content is not None:
                post["content"] = content

            return jsonify(post), 200

    return jsonify({"error": "Post not found"}), 404


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """
    Search posts by title and/or content.
    Provide 'title' and/or 'content' as query parameters.
    Returns all posts that match the criteria, or an empty list if none do.
    """
    title_query = request.args.get('title', None)
    content_query = request.args.get('content', None)

    if not title_query and not content_query:
        return jsonify(POSTS)

    filtered_posts = POSTS

    if title_query:
        filtered_posts = [post for post in filtered_posts if title_query in post["title"]]

    if content_query:
        filtered_posts = [post for post in filtered_posts if content_query in post["content"]]

    return jsonify(filtered_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
