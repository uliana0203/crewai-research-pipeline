# src/research_team/crew.py
from __future__ import annotations
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ScientificPaperProject:
    """ScientificPaperProject crew"""

    agents_config_path = "config/agents.yaml"
    tasks_config_path = "config/tasks.yaml"

    @agent
    def literature_analyst(self) -> Agent:
        return Agent(config=self.agents_config["literature_analyst"], verbose=True)

    @agent
    def methodology_designer(self) -> Agent:
        return Agent(config=self.agents_config["methodology_designer"], verbose=True)

    @agent
    def data_analyst(self) -> Agent:
        return Agent(config=self.agents_config["data_analyst"], verbose=True)

    @agent
    def research_lead(self) -> Agent:
        return Agent(config=self.agents_config["research_lead"], verbose=True)

    @agent
    def results_writer(self) -> Agent:
        return Agent(config=self.agents_config["results_writer"], verbose=True)

    @agent
    def language_editor(self) -> Agent:
        return Agent(config=self.agents_config["language_editor"], verbose=True)

    @agent
    def citation_manager(self) -> Agent:
        return Agent(config=self.agents_config["citation_manager"], verbose=True)

    @agent
    def ethics_officer(self) -> Agent:
        return Agent(config=self.agents_config["ethics_officer"], verbose=True)

    @agent
    def peer_reviewer(self) -> Agent:
        return Agent(config=self.agents_config["peer_reviewer"], verbose=True)

    @agent
    def project_manager(self) -> Agent:
        return Agent(config=self.agents_config["project_manager"], verbose=True)
    
    @agent
    def manuscript_assembler(self) -> Agent:
        return Agent(config=self.agents_config["manuscript_assembler"], verbose=True)

    
    @task
    def search_task(self) -> Task:
        return Task(config=self.tasks_config["search_task"])

    @task
    def outline_task(self) -> Task:
        return Task(config=self.tasks_config["outline_task"])

    @task
    def methodology_task(self) -> Task:
        return Task(config=self.tasks_config["methodology_task"])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config["analysis_task"])

    @task
    def results_task(self) -> Task:
        return Task(config=self.tasks_config["results_task"])

    @task
    def editing_task(self) -> Task:
        return Task(config=self.tasks_config["editing_task"])

    @task
    def citation_task(self) -> Task:
        return Task(config=self.tasks_config["citation_task"])
    
    @task
    def assemble_manuscript_task(self) -> Task:
        return Task(config=self.tasks_config["assemble_manuscript_task"])
    
    @task
    def ethics_task(self) -> Task:
        return Task(config=self.tasks_config["ethics_task"])

    @task
    def review_task(self) -> Task:
        return Task(config=self.tasks_config["review_task"])

    @task
    def submission_checklist_task(self) -> Task:
        return Task(config=self.tasks_config["submission_checklist_task"])
    
    @task
    def cover_letter_task(self) -> Task:
        return Task(config=self.tasks_config["cover_letter_task"])
    
   

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
