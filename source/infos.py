class DocumentInfos:

    title = u'Documentation'
    first_name = 'Cédric'
    last_name = 'Donner'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'October'
    seminary_title = u'PyRobotSim'
    tutor = u""
    release = "0.1"
    repository_url = "https://github.com/donnerc/pyrobotsim-docs"
    language = 'en'

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()