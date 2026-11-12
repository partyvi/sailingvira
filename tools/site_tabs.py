"""Site tabs, shared by the site build and the Blogger diary theme.

(key, site-relative slug, labels). The "diary" tab (slug None) goes to the Blogger diary.
"""
TABS = [("home", "", {"en": "Home", "ua": "Головна"}),
        ("boat", "boat/", {"en": "The Boat", "ua": "Човен"}),
        ("projects", "projects/", {"en": "Projects", "ua": "Проєкти"}),
        ("sailing", "voyages/", {"en": "Sailing", "ua": "Плавання"}),
        ("diary", None, {"en": "Boat diary", "ua": "Щоденник"}),
        ("workshop", "workshop/", {"en": "Workshop", "ua": "Майстерня"}),
        ("videos", "videos/", {"en": "Videos", "ua": "Відео"}),
        ("about", "about/", {"en": "About me", "ua": "Про мене"}),
        ("contact", "contact/", {"en": "Contact", "ua": "Контакти"})]
