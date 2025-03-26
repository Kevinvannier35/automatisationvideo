from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/process-video', methods=['POST'])
def process_video():
    video = request.files['video']
    input_path = '/tmp/input.mp4'
    output_path = '/tmp/output.mp4'

    video.save(input_path)

   result = subprocess.run([
    'ffmpeg', '-y', '-loglevel', 'debug', '-i', input_path,
    '-vf', 'eq=saturation=1.5:contrast=1.2',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-profile:v', 'main',
    '-level', '3.1',
    '-crf', '23',
    '-preset', 'medium',
    '-movflags', '+faststart',
    '-c:a', 'aac',
    '-b:a', '128k',
    output_path
], check=True, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)




    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
