# app.py

from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# Mock incident data
mock_incidents = [
    {"id": 1, "severity": "High", "description": "Unauthorized access attempt detected."},
    {"id": 2, "severity": "Medium", "description": "Malware detected on endpoint."},
    {"id": 3, "severity": "Low", "description": "Potential phishing email reported by user."},
]

@app.route('/')
def index():
    return render_template('index.html', incidents=mock_incidents)

@app.route('/incident/<int:incident_id>')
def incident_detail(incident_id):
    # Fetch incident details from a hypothetical incident management system
    incident = next((incident for incident in mock_incidents if incident['id'] == incident_id), None)
    if incident:
        return render_template('incident_detail.html', incident=incident)
    else:
        return "Incident not found.", 404

@app.route('/triage', methods=['POST'])
def triage():
    if request.method == 'POST':
        incident_id = request.form['incident_id']
        triage_action = request.form['triage_action']
        # Perform triage action (e.g., assign, close) on the incident
        # This could involve making API calls to an incident management system
        return redirect(url_for('incident_detail', incident_id=int(incident_id)))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
