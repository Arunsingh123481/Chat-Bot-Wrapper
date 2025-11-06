🖥️ Running This Chatbot on Another Windows Computer (Local Setup)

If you want to run this chatbot on another Windows PC (for example, your friend’s laptop or another system in your home), follow these steps carefully 👇

### 1️⃣ Copy the Project Folder
Copy the entire project folder (e.g. `Chat-Bot-Wrapper`) to the new system using:
- GitHub clone

The folder should contain:
```
Chat-Bot-Wrapper/
│
├── gemini_chatbot.py
├── README.md
├── requirements.txt
└── (optional) assets/

````

---

### 2️⃣ Install Python
Download and install **Python 3.10 or newer** from:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

✅ During installation, make sure you tick **“Add Python to PATH”**.

---

### 3️⃣ Create a Virtual Environment
Open **Command Prompt** in your project folder and run:

```bash
python -m venv venv
````

Then activate it:

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

Now install all required packages:

```bash
pip install -r requirements.txt
```

(If there’s no `requirements.txt`, run:)

```bash
pip install streamlit google-genai
```

---

### 5️⃣ Set the Gemini API Key

Get your **Gemini API key** from Google AI Studio:
👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Then set it permanently on the new system:

```bash
setx GEMINI_API_KEY "AIzaSyCEY-UGJT3qDIauZgLd2DsK7p-Vo_R37Lo"

```

✅ After setting it, **close and reopen Command Prompt** to apply the change.

---

### 6️⃣ Run the Chatbot

In your project folder, type:

```bash
streamlit run gemini_chatbot.py
```

It will automatically open in your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

### ✅ Optional: Access from Another PC on the Same Wi-Fi

If you want others on the same Wi-Fi network to access your chatbot, run:

```bash
streamlit run gemini_chatbot.py --server.address=0.0.0.0 --server.port=8501
```

Then on another computer’s browser, open:

```
http://YOUR_PC_IP:8501
```

(Find your IP using `ipconfig` in Command Prompt.)

---

That’s it! 🎉
Your Gemini chatbot will now work on any Windows computer with just Python and the Gemini API key.

```

---

Would you like me to include a **“For Linux / macOS users”** version right after this (so your README works cross-platform too)?
```
