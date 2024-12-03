"""Fills in an HTML template with user data to construct a custom webpage."""

# Collect user profile data.
first_name = input("あなたの名前は何ですか？ ")

# Construct a personalized page header for the logged in user.
header_title =テストのSNSです"<h1>Guest's profile</h1>"
header_subtitle = "<h2>Hello, " + first_name + "!</h2>"
header_content = "<p>unknown@example.com</p>"
page_header = header_title + header_subtitle + header_content

# Construct the main profile page content.
section_title = "<h2>ゲストについて</h2>"
section_text = "<p>This is a cool bio.</p>"
button = "<button>Like</button>"
section_footer = "<p>Notifications: 4</p>"
page_content = section_title + section_text + button + section_footer

# The final HTML body combines all the elements, in order.
print("The HTML string for your profile page is:")
print(page_header + page_content)
