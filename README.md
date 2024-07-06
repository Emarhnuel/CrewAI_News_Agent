This project leverages CrewAI, a framework for building autonomous AI agents, to generate insightful news articles on a given tech topic.

## Key Features:
* Automated Research and Writing: The agent autonomously conducts research on the specified topic using the SerperDevTool for web searches, then drafts a well-structured news article.



* LLM Integration: Utilizes the Google Gemini Pro language model (via `langchain_google_genai`) for natural language understanding and generation.


* Task Specialization: Employs two specialized agents:
  * `news_researcher`: Focused on identifying and analyzing trends in the given topic.
  * `news_writer`: Crafts engaging and informative articles based on the research findings.
  * Customizable Output: The generated article is saved in markdown format, allowing for easy customization and publishing.
  

## Installation & Usage:
1.  Clone the Repository:

``` Bash
git clone https://github.com/Emarhnuel/CrewAI_News_Agent.git
```


2. Install Dependencies:

``` Bash
pip install -r requirements.txt
```


3. Set Up Environment Variables:

  * Create a `.env` file in the project root directory.
  * Add your Google API key (`GOOGLE_API_KEY`) and Serper API key (`SERPER_API_KEY`) to the `.env` file.


4. Run the Agent:

``` Bash
python crew.py
```


## Configuration:
  * Topics: Modify the `topic` variable in `crew.py` to specify the desired tech topic for research.
  * Agent Behavior: Fine-tune agent roles, goals, and backstory in `agents.py`.
  * Task Details: Adjust task descriptions and expected outputs in `tasks.py`.
  * Output Customization: Customize the output format in `tasks.py`.