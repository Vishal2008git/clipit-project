from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/download')
def download_video():
    video_url = request.args.get('url')
    format = request.args.get('format', 'mp4')  # Default to 'mp4'

    if not video_url:
        return "Error: No URL provided.", 400

    # Your yt-dlp logic to download the video
    options = {
        'format': format,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_url = info_dict['formats'][0]['url']
    except Exception as e:
        return f"Error occurred: {str(e)}", 500

    return send_file(video_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # <-- Modified line
