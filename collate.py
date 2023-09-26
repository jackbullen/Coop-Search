import os
import json

def get_posting(file):
    co0p_job = dict()

    with open(file, 'r') as f:
        text = f.read()
        try:
            info, desc = text.split('Job Description:')
        except:
            info1, info2, desc = text.split('Job Description:')
            info = info1 + info2
        info = info.split(':')
        
        co0p_job['org'] = text.split('Organization Name')[-1].split('\n')[0]

        new_info = []
        for i in range(1, len(info)):
            info[i] = info[i].split('\n')
            try:
                new_info.append(info[i][-1] + info[i+1].split('\n')[0])
            except:
                pass

        if desc[0] == ' ':
            desc = desc[1:]

        co0p_job.update({'info': new_info, 'description': desc})

        return co0p_job
    
JOBS = dict()
for _,_,files in os.walk('./postings'):
    for file in files:
        if file.endswith('.txt'):
            JOBS[file.split('.')[0].split('_')[-1]] = get_posting('postings'+'/'+file)

with open('jobs.json', 'w') as f:
    json.dump(JOBS, f)