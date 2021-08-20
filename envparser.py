class EnvParser:
    @staticmethod
    def parse(filename='.env'):
        envs = {}
        with open(filename, 'r', encoding='utf8') as file:
            for line in file.readlines():
                env = line.split('=')
                envs[env[0]] = env[1][:len(env[1])-1]
        return envs
