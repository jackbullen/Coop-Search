import os

with open('./latex_template.txt', 'r') as f:
    LATEX = f.read()

for _,_,files in os.walk('./modified_cover_letters'):
    for file in files:
        OUTTEX = LATEX.split('--!!--')[0]

        with open(f'./modified_cover_letters/{file}', 'r') as f:
            content = f.read()

            OUTTEX +=  ('\n\n'+r'\vspace{1em}'+'\n\n').join('\n\n'.join([x for x in content.split('Dear')[0].split('\n\n')]).split('\n\n'))

            for i, paragraph in enumerate(content.split('Dear')[1].split('\n')):
                if i == 0:
                    paragraph = 'Dear ' + paragraph
                OUTTEX += r'\noindent' + '\n ' + paragraph + '\n' + r'\vspace{1em}'
        num = file.split('.')[0][-3:]
        os.makedirs(f'./docs/CL_{num}', exist_ok=True)
        with open(f'./docs/CL_{num}/cover_letter_' + file.split('.')[0] + '.tex', 'w') as f:
            f.write(OUTTEX+r'\end{document}')