import streamlit as st
from hydralit import HydraApp

from cameroon import cameroon_app
from home_page.landing import landing_app
from kenya import kenya_app
from madagascar import madagascar_app
from namibia import namibia_app
from south_africa import south_app
from users.login_app import LoginApp
from users.signup import SignUpApp

if __name__ == "__main__":

    # this is the host application, we add children to it and that's it!
    app = HydraApp(title="Biospacy", favicon="./images/favicon.ico")

    # add all your application classes here
    app.add_app("home", icon="?", app=landing_app())
    app.add_app("South Africa", icon="?", app=south_app())
    app.add_app("Kenya", icon="?", app=kenya_app())
    app.add_app("Cameroon", icon="?", app=cameroon_app())
    app.add_app("Namibia", icon="?", app=namibia_app())
    app.add_app("Madagascar", icon="?", app=madagascar_app())

    # app.add_app("Sample App",icon="?", app=MySampleApp())
    app.add_app(
        "Signup", icon="?️", app=SignUpApp(title="Signup"), is_unsecure=True
    )

    # we want to have secure access for this HydraApp, so we provide a login application
    # optional logout label, can be blank for something nicer!
    app.add_app("Login", app=LoginApp(title="Login"), is_login=True)

    # and finally just the entire app and all the children.

    # run the whole lot
    app.run()
