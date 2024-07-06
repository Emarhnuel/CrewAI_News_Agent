from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
import agentops

agentops.init(tags=["crewai-agent"])


## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    verbose=2,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in Fintech'})
print(result)

agentops.end_session("Success")
