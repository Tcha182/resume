import streamlit as st
import base64

from datetime import date
 
st.set_page_config(page_title='CV Corentin de Tilly', page_icon='👨‍💼')

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


# Calculate my age dynamically

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
     
my_age = calculateAge(date(1994, 2, 4))


#####################
# Navigation

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #6699CC;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/corentin-de-tilly/?locale=en_US" target="_blank">Corentin de Tilly</a>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Header 
st.write('''
# Corentin Récopé de Tilly-Blaru
##### *Curriculum Vitae* 
''')

with open("cdt.png", 'rb') as f:
        image = f.read()

image_bytes = base64.b64encode(image).decode()
local_file = f'<p style="text-align:center;"><img src="data:image/jpeg;base64,{image_bytes}" alt="Image" width = 150> </p>'
st.markdown(local_file, unsafe_allow_html = True)

st.write(f'###### {my_age} years old')

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
Passionate Data Scientist, with extensive experience in data analysis, business intelligence and project management, looking for a data related position starting end of 2022.
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
  col1, col2, col3 = st.columns([1.5,2,2])
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
'2021-2022')
st.markdown('''
- programming (Python), dataviz, machine learning, big data, deep learning, reinforcement learning.
- Graduation project (team of 3): "Tennis betting – Beat the bookmakers with data science".
- `9 months` training.
''')

txt('**Bachelor of Business Administration** - *NEOMA Business School* - Reims, FRANCE',
'2012-2017')
st.markdown('''
- Major: International Business Management.
- Minor: European Union Policy.
- `2 years` exchange as a double degree student in Breda 🇳🇱.
''')



#####################
st.markdown('''
## Work Experience
''')

txt('**Data Project Manager**, *Renault Group*, Boulogne-Billancourt, FRANCE',
'2021-2022')
st.markdown('''
- Ad-hoc data science projects for the VP Finance of Renault Group.
- Financial & commercial modelling and forecasting.
- Algorithmic business analytics - worldwide scope, all business units: `46bn€ turnover`, `2.7m units` sold in 2021.
''')


txt('**Project Manager Digital and Transformation Europe**, *Renault Group*, Boulogne-Billancourt, FRANCE',
'2020-2021')
st.markdown('''
- Business Intelligence - design and deployment of analytical tools for the controlling teams in Europe: `150+ users`. Quick developments using agile methodology. 
- Definition of the `5 years` digital roadmap for the Europe region.
- Management of a finance community to share best practices, methods, and tools.
- Report automation, including algorithmic comments and scheduled updates.
- Direct management of `2` successive apprentices and `1` intern.

''')


txt('**Marketing Business Controller**, *Renault Nederland*, Amsterdam, the NETHERLANDS',
'2018-2019')

st.markdown('''
- Financial modelling. Budgeting and commercial forecasting.
- Improvement of the analytical tools and methods.
- Monthly closures, follow-up of the activity and monitoring of the provisions.
- Analysis of the results and data mining, production of reports and insights to optimize commercial actions, pricing, model mix, equipment, engine mix, customer mix and car flow. 
- Control and monitoring of the marketing budgets in direct relation with the departments managers and the Benelux Marketing Director.
''')


txt('**Assistant Controller**, *Renault Benelux*, Amsterdam, the NETHERLANDS', 
'2017-2018')
st.markdown('''
- Monthly closing for Renault Belgium/Luxembourg in Brussels, internal control for the Benelux Cluster. Support for the Benelux head of control and CFO. 
''')


txt('**Junior Finance Controller**, *Renault Nederland*, Amsterdam, the NETHERLANDS',
'2017')
st.markdown('''
- Improvement of the reporting process, development of new financial analysis tools. Significant efficiency gains, as well as overall reporting quality improvement.
''')


txt('**Private Equity Intern**, *Linked to Africa Management Services*, Cape Town, SOUTH AFRICA',
'2016')
st.markdown('''
- Management of small and medium size (`USD 5M<EV<50M`) Private Equity investment projects.
- Due diligence, financial modelling.
- Direct contact with investors, promotors, and other stakeholders at every step of the investment process.
''')


txt('**Receptionist**, *Centre Sports et Loisirs de la Banque de France*, Bougival, FRANCE',
'2015')
st.markdown('''
- Clients (Banque de France employees) reception and information.
- Management of the Sports Club’s memberships.
- Summer job.
''')


txt('**Sales Manager Assistant**, *Champagne Boizel*, Épernay, FRANCE',
'2013')
st.markdown('''
- Sale of Champagne (B2B). Clients’ management.
- Implementation of a new website and online shop.
- Monitoring of Boizel’s participation in major events such as the Grand Tasting 2013 in le Louvre, Paris.
''')


txt('**Intern**, *Château de Vallery*, Vallery, FRANCE',
'2013')
st.markdown('''
- Events planning and management (high budget weddings).
- Promotion of the Château, design and realisation of a targeted campaign, which resulted in `2` additional bookings.
- Summer internship.
''')


#####################

# st.markdown(''' ## Projects ''')
# txt4('Connect4 agent', 'An agent to play connect4, ranked in `top 10%` on kaggle ConnectX competition', 'https://www.kaggle.com/competitions/connectx/leaderboard')


#####################
st.markdown('''
## Skills
''')

txt3('Languages', '`French`: native language')
txt3('', '`English`: fluent')


txt3('Programming', '`Python`, `VBA`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`, `DAX`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Business Intelligence', '`Power BI`, `Spotfire`, `Tableau`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`Streamlit`, `Heroku`, `GCP`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/corentin-de-tilly/?locale=en_US')
