
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    script_path = request.args.get('script')
    try:
        # Run the Python script using subprocess
        subprocess.run(['python', script_path], check=True)
        return jsonify({'success': True, 'message': f'Successfully ran {script_path}'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)})

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)