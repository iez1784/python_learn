__author__ = 'zhangedison'

import gitlab
import time

gl = gitlab.Gitlab('http://192.168.1.6/', private_token='pM9xjcb9tcxD4y6JzATv')


print(gl)

groups = gl.groups.get(4)
print(groups)

projects = groups.projects.list()

for project in projects:
    print(project.id)

    name = project.id

    # Create the export
    p = gl.projects.get(name)
    print(p)
    export = p.exports.create({})
    file = str(name) + '_export.tgz'

    # Wait for the 'finished' status
    export.refresh()
    while export.export_status != 'finished':
        time.sleep(1)
        export.refresh()

    # Download the result
    with open(file, 'wb') as f:
        export.download(streamed=True, action=f.write)











