from Webscraper import JobScraper




class Healthcare(JobScraper):
    def __init__(self):
        super().__init__("Healthcare")


class Projects(JobScraper):
    def __init__(self):
        super().__init__("Project")


class Analyst(JobScraper):
    def __init__(self):
        super().__init__("Analyst")


an = Analyst()
hea = Healthcare()
pro = Projects()


if __name__ == "__main__":
    hea.startp()
    an.startp()
    pro.startp()

