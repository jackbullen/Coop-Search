---> ---> ---> ---> ---> ---> ---> ---> ---> ---> ---> ---> ---> ---> --->
|collect jobs| get/process custom cover letter | place into latex document |
|------------|--------------------------------|--------------------------|
| scrape.py           |   modify_cl.py                             |           create_doc.py               |
| collate.py           |             process_cl.py                   |                          |

# Todo
- Fix vspace doubles in create_doc.py
- Use resume alongside base_cover_letter.txt  and job description to generate cover letter
- Include resume in latex doc
- Scrape more job boards
- Add more customization options

# Usage
1. Place job descriptions into `postins/posting_id`
2. Run `python3 modify_cl.py <posting_id>`
3. Run `python3 create_doc.py`
4. Edit the formatting and content in the generated tex file.

<img width="818" alt="demo" src="https://github.com/jackbullen/Coop-Search/assets/37254717/73102481-b8a5-4456-b194-0f8ea82b3d71">


<img width="522" alt="chat" src="https://github.com/jackbullen/Coop-Search/assets/37254717/bcda10fd-6ec8-4310-8add-ac9718c02821">
