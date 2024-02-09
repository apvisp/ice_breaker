from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> tr:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = "given the full name of a person I want you to get me a link to their LinkedIn page. Your answer shuold be a URL"

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url,
            description="Useful for when you need the Linkedin page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url
