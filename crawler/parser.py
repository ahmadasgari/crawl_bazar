BASE_LINK = 'https://cafebazaar.ir/app/'


class Parser:

    @staticmethod
    def link_parser(data):

        link_list = list()

        data = data['singleReply']['getPageV2Reply']['page']['pageBodyInfo'][
            'pageBody']['rows']

        for d in data:
            apps = d.get('simpleAppList')
            if apps:

                for app in apps.get('apps'):
                    link_list.append(BASE_LINK + app['info']['packageName'])

        return link_list

    def data_parser(self, data):
        pass
