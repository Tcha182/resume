import streamlit as st
from PIL import Image
from datetime import date
import base64
from io import BytesIO
import requests

@st.cache_data
def image_to_base64(img_path):
    with Image.open(img_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode()

im = Image.open("favicon.ico")
st.set_page_config(page_title='CV Corentin de Tilly', page_icon=im)

# linkedin_data = image_to_base64('linkedin.png')
# github_data = image_to_base64('github.png')

linkedin_svg = open("linkedin.svg", "r").read()
github_svg = open("github.svg", "r").read()

form_url = "https://formsubmit.co/el/wixece"

# Apply custom CSS
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def navbar3():

  st.markdown(f"""
  <body>

  <div class="custom-navbar">
      <a href="#2acaf448" class="logo">Corentin de Tilly</a>
      <input type="checkbox" class="menu-btn" id="menu-btn">
      <label for="menu-btn" class="menu-icon">
          <span></span>
      </label>
      <ul>
          <li><a href="#education">Education</a></li>
          <li><a href="#work-experience">Work Experience</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#interests">Interests</a></li>
          <li><a href="{form_url}">Contact</a></li>
          <li class="nav-icon">
          <a href="https://www.linkedin.com/in/corentin-de-tilly/?locale=en_EN" target="_blank" rel="noopener noreferrer" class="icon-link">
              {linkedin_svg}
          </a>
          </li>
          <li class="nav-icon">
              <a href="https://github.com/Tcha182" target="_blank" rel="noopener noreferrer" class="icon-link">
                  {github_svg}
              </a>
          </li>
      </ul>
  </div>
      """,unsafe_allow_html=True)

navbar3()

# Calculate age dynamically
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

my_age = calculateAge(date(1994, 2, 4))



# Header 
st.markdown('''
# Corentin Récopé de Tilly-Blaru
##### *Curriculum Vitæ* 
''')

with open("cdt.png", 'rb') as f:
        image = f.read()

image_bytes = base64.b64encode(image).decode()
local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width = 150> </p>'
st.markdown(local_file, unsafe_allow_html = True)

st.markdown(f'###### {my_age} years old')

d1, d2, d3 = st.columns(3)


st.markdown('## Summary')
st.info('''
"Driven by a passion for understanding, I transform vast amounts of data into actionable insights. Whether developing strategies, leading analytical teams, or optimizing existing resources, my mission remains consistent: to empower organizations with clear, data-driven decisions."
''')

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,3,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Data Scientist** - *Mines Paris* / *DataScientest* - Paris, FRANCE',
'**2021-2022**')
st.markdown('''
- programming (Python), machine learning, big data, deep learning, reinforcement learning, dataviz.
- Graduation project (team of 3): "Tennis betting – Beat the bookmakers with data science".
- `9 months` training.
''')

txt('**Bachelor of Business Administration** - *NEOMA Business School* - Reims, FRANCE',
'**2012-2017**')
st.markdown('''
- Major: International Business Management.
- Minor: European Union Policy.
- `2 years` exchange as a double degree student in Breda :flag-nl:.
''')



#####################
st.markdown('''
## Work Experience
''')

txt('**Data Analyst**, *RATP Dev*, Paris, FRANCE',
'**2023-Present**')
st.markdown('''
- Lead and manage data analysis and data science projects for RATP Dev and its subsidiaries, overseeing all phases from conception to deployment.
- Management of `1` Data Analyst.
- Focus areas include IoT, predictive maintenance, natural language processing, and passenger flow analysis.
''')

txt('**Data Project Manager**, *Renault Group*, Boulogne-Billancourt, FRANCE',
'**2021-2022**')
st.markdown('''
- Executed ad-hoc data science projects for the VP Finance, enhancing financial and commercial modeling and forecasting.
- Algorithmic business analytics - worldwide scope, all business units: `46bn€ turnover`, `2.7m units` sold in 2021.
''')


txt('**Project Manager Digital and Transformation Europe**, *Renault Group*, Boulogne-Billancourt, FRANCE',
'**2020-2021**')
st.markdown('''
- Designed and deployed analytical tools for the controlling teams in Europe: `150+ users`.
- Defined the `5-year` digital roadmap for the Europe region.
- Managed a finance community to share best practices, methods, and tools.
- Automated reporting processes, incorporating algorithmic comments and scheduled updates.
- Supervised two successive apprentices and one intern.

''')


txt('**Marketing Business Controller**, *Renault Nederland*, Amsterdam, the NETHERLANDS',
'**2018-2019**')

st.markdown('''
- Developed financial models, budgeting, and commercial forecasting.
- Enhanced analytical tools and methods.
- Conducted monthly closures, activity follow-ups, and provision monitoring.
- Analyzed results and produced reports to optimize commercial actions, pricing, model mix, equipment, engine mix, customer mix, and car flow.
- Controlled and monitored marketing budgets, coordinating directly with department managers and the Benelux Marketing Director.
''')


txt('**Assistant Controller**, *Renault Benelux*, Amsterdam, the NETHERLANDS', 
'**2017-2018**')
st.markdown('''
- Managed monthly closing for Renault Belgium/Luxembourg in Brussels and internal control for the Benelux Cluster.
- Supported the Benelux head of control and CFO.
''')


txt('**Junior Finance Controller**, *Renault Nederland*, Amsterdam, the NETHERLANDS',
'**2017**')
st.markdown('''
- Improved reporting processes and developed new financial analysis tools, resulting in significant efficiency gains and enhanced reporting quality.
''')


txt('**Private Equity Intern**, *Linked to Africa Management Services*, Cape Town, SOUTH AFRICA',
'**2016**')
st.markdown('''
- Managed private equity investment projects for small and medium-sized enterprises(`USD 5M<EV<50M`).
- Conducted due diligence and financial modeling.
- Maintained direct contact with investors, promoters, and stakeholders throughout the investment process.
''')


txt('**Receptionist**, *Centre Sports et Loisirs de la Banque de France*, Bougival, FRANCE',
'**2015**')
st.markdown('''
- Handled client reception and information for Banque de France employees.
- Managed Sports Club memberships.
- Summer job.
''')


txt('**Sales Manager Assistant**, *Champagne Boizel*, Épernay, FRANCE',
'**2013**')
st.markdown('''
- Facilitated B2B champagne sales and client management.
- Implemented a new website and online shop.
- Monitored Boizel’s participation in major events, such as the Grand Tasting 2013 in the Louvre, Paris.
''')


txt('**Intern**, *Château de Vallery*, Vallery, FRANCE',
'**2013**')
st.markdown('''
- Planned and managed high-budget weddings and events.
- Promoted the Château and designed a targeted campaign, resulting in two additional bookings.
- Summer internship.
''')


#####################

st.markdown(''' ## Projects ''')

txt4('Face quiz', 'A GPT-powered game in which the goal is to identify well-known individuals using a portrait and a tagline.', 'Available [here](https://facequiz.streamlit.app//).')

txt4('Connect4 agent', 'A Python agent to play connect4. It ranked in the `top 10%` of the Kaggle [ConnectX](https://www.kaggle.com/competitions/connectx/leaderboard) competition.', 'Try it [here](https://connect4.streamlit.app/) (desktop).')


#####################
st.markdown('''
## Skills
''')

txt3('Languages', '`French`: native language')
txt3('', '`English`: fluent')


txt3('Programming', '`Python`, `VBA`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `DAX`')
txt3('Data visualization', '`plotly`, `seaborn`')
txt3('Business Intelligence', '`Power BI`, `Spotfire`, `Tableau`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`Django`, `Streamlit`, `Docker`, `GCP`')


#####################
st.markdown('''
## Interests
''')

txt('**Sports**', "")

txt3('Sailing (skipper)', '2023: Grenadines Islands - STAR VI *Lagoon 42* - crew of `9`')
txt3('', '2022: South Brittany - Camanoe 3 *RM 890* - crew of `2`')
txt3('Climbing', 'top rope `7a`, lead climbing `6b`, bouldering `6b`')
txt3('Kitesurfing', '')
txt3('Diving', '`PADI advanced`')
txt3('Kick Boxing',"")

txt('**Hobbies**', "")

st.markdown('Piano, Travelling, Raspberry pi, Crafting')

txt('**Others**', "")
st.markdown('Licensed driver')


#st.markdown(''' ## Contact ''')

d2.link_button(":mailbox: Contact me", form_url, use_container_width=True)
