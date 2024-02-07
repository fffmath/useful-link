import yaml

# Read YAML files
with open('./data/sites.yml', 'r') as yaml_file:
    # Load YAML data into Python data structures using the load function
    data_sites = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Read YAML files
with open('./data/courses.yml', 'r') as yaml_file:
    # Load YAML data into Python data structures using the load function
    data_courses = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Read YAML files
with open('./data/scholars.yml', 'r') as yaml_file:
    # Load YAML data into Python data structures using the load function
    data_scholars = yaml.load(yaml_file, Loader=yaml.FullLoader)
    
# Sort scholars by last name
data_scholars['scholars'] = sorted(data_scholars['scholars'], key=lambda x: x['name'].split()[-1])

# Generate HTML content for sites
html_content_sites= ""
for site in data_sites['sites']:
    html_content_sites += f"""
    <mochi-box shiba="random"> 
        <div class="circle"></div>
        <h3>{site['name']}</h3>
        <a class="shop site" title="site" target="_blank" href="{site['link']}">{site['tag']}</a>
        <h2>{site['intro']}</h2>
        <button>
            <a target="_blank" href="{site['link']}">Show more</a>
        </button>
    </mochi-box>
    """

# Generate HTML content for courses
html_content_courses= ""
for course in data_courses['courses']:
    html_content_courses += f"""
    <mochi-box shiba="random"> 
        <div class="circle"></div>
        <h3>{course['name']}</h3>
        <a class="shop site" title="site" target="_blank" href="{course['link']}">{course['tag']}</a>
        <h2>{course['intro']}</h2>
        <button>
            <a target="_blank" href="{course['link']}">Show more</a>
        </button>
    </mochi-box>
    """

# Generate HTML content for scholars
html_content_scholars= ""
for person in data_scholars['scholars']:
    html_content_scholars += f"""
    <mochi-box shiba="random"> 
        <div class="circle"></div>
        <h3>{person['name']}</h3>
        <a class="shop site" title="site" target="_blank" href="{person['dblp']}">dblp</a>
        <h2>{person['intro']}</h2>
        <button>
            <a target="_blank" href="{person['link']}">Show more</a>
        </button>
    </mochi-box>
    """

# Read the original HTML file
with open('original.html', 'r') as original_html_file:
    original_html = original_html_file.read()

# Find the specified locations and insert HTML content
insertion_index_sites = 1 + original_html.find('<h1>USEFUL SITE FOR CRYPTO</h1>')
insertion_index_sites += 1 + len('<h1>USEFUL SITE FOR CRYPTO</h1>')  # Move the index after the closing tag
insertion_index_sites += 1 + len('<p class="sub">You can find the latest news and advanced knowledge here.</p> ')  # Move the index after the closing tag

insertion_index_courses = 1 + original_html.find('<h1>COURSES FOR CRYPTO</h1>')
insertion_index_courses += 1 + len('<h1>COURSES FOR CRYPTO</h1>')  # Move the index after the closing tag
insertion_index_courses += 1 + len('<p class="sub">Links to some open cryptography courses, and gratitude for their hard work.</p>')  # Move the index after the closing tag

insertion_index_scholars = 1 + original_html.find('<h1>BLOG ABOUT CRYPTO</h1>')
insertion_index_scholars += 1 + len('<h1>BLOG ABOUT CRYPTO</h1>')  # Move the index after the closing tag
insertion_index_scholars += 1 + len('<p class="sub">Other people\'s personal homepage (mainly for cryptography professionals).</p>')  # Move the index after the closing tag

# Update the HTML content
updated_html = original_html[:insertion_index_sites] + html_content_sites + original_html[insertion_index_sites:insertion_index_courses] + html_content_courses + original_html[insertion_index_courses:insertion_index_scholars] + html_content_scholars + original_html[insertion_index_scholars:]

# Write the updated HTML content to a new HTML file
with open('index.html', 'w') as updated_html_file:
    updated_html_file.write(updated_html)
