from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("\n" + "=" * 50)
print("Loading AI model...")
print("=" * 50)

try:
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    model_name = "joeddav/distilbert-base-uncased-go-emotions-student"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    print("✓ Model loaded successfully!")
    print("=" * 50 + "\n")
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nRun: pip install transformers torch")
    exit(1)


def detect_emotions(text, threshold=0.75):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits)[0].tolist()
    labels = model.config.id2label
    return [labels[i] for i, p in enumerate(probs) if p > threshold]


@app.route('/api/analyze', methods=['POST', 'OPTIONS'])
def analyze_text():
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        print(f"\n Received: {data}")

        if not data or 'message' not in data:
            return jsonify({'success': False, 'error': 'No message'}), 400

        message = data['message']
        threshold = data.get('threshold', 0.75)

        emotions = detect_emotions(message, threshold)
        print(f"✓ Emotions: {emotions}")

        return jsonify({
            'success': True,
            'emotions': emotions,
            'message': message
        }), 200

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model': model_name}), 200


@app.route('/')
def home():
    return jsonify({'message': 'Emotion API Running', 'version': '1.0'}), 200


if __name__ == '__main__':
    print("Server running on http://localhost:5000\n")
    app.run(debug=True, port=5000, host='127.0.0.1')