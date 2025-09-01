# 🏛️ The Council

**The Council** is a multi-agent system built using the [Swarms](https://github.com/kyegomez/swarms) framework and Streamlit.  
The project simulates a "council meeting" where multiple AI agents deliberate on a user’s query and provide diverse perspectives—ranging from overviews and pros/cons to practical feasibility and expert advice—before delivering a final consensus.

---

## 🚀 Features

- **Multi-agent collaboration**
  - 📝 **Overview Agent** → Summarizes the query clearly.  
  - ⚖️ **Pros & Cons Agent** → Outlines advantages and disadvantages.  
  - 🔧 **Practical Agent** → Evaluates technical, economic, environmental, and social feasibility.  
  - 🎓 **Expert Agent** → Provides in-depth expert-level insights and best practices.  
  - 🏁 **Arbitrator Agent** → Synthesises all viewpoints into a clear, actionable recommendation.  

- **Interactive UI**
  - Built with **Streamlit** for a clean, tabbed interface.  
  - Separate tabs for each agent’s response.  
  - Spinner feedback while the council deliberates.  

- **Extensible**
  - Easily add/remove agents.  
  - Swap out models or expand the council with new roles.  

---

## 📂 Project Structure
```
├── agents.py          # Defines the agents and their roles
├── dashboard.py       # Streamlit dashboard for UI
├── .env               # API keys and environment variables
└── README.md          # This file
```

---

## ⚙️ Installation & Setup
### 1. Clone the repository
```
git clone https://github.com/rajan-bhateja/The-Council.git
cd The-Council
```
### 2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Set up environment variables
```
OPENAI_API_KEY=your_openai_api_key
```
### 5. Run the Streamlit app
```
streamlit run .\dashboard.py
```

---

## 🛠️ How It Works

User submits a query via the Streamlit UI.

The query is passed into the workflow (`InteractiveGroupChat`) that cycles through all agents.

Each agent responds from its unique perspective.

The Consensus Agent reads all outputs and provides a final verdict.

---

## 🌟 Future Improvements

* Add debate mode → agents can reply to one another before consensus.
* Add memory → carry context across multiple queries in a session.
* Allow custom arbiter styles → e.g., decisive, risk-averse, optimistic.
* Export council discussion to Markdown/PDF for sharing.

---

## 📜 License

MIT License. Feel free to fork, modify, and use in your own projects.

---

## 🙌 Acknowledgements

Swarms:
  for the multi-agent framework.

Streamlit:
  for the web app framework.

OpenAI:
  for LLM powering the agents.

---
