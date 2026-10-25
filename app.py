
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kali Linux Guide",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kali Linux Guide</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            background-color: #101820;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            text-align: center;
        }

        header {
            background-color: #00a8a8;
            padding: 25px;
        }

        h1 {
            color: white;
            margin-top: 0;
        }

        main {
            padding: 30px 20px;
            min-height: 420px;
        }

        h2 {
            color: #00ffff;
            margin-top: 25px;
        }

        p {
            font-size: 18px;
            line-height: 1.6;
        }

        a {
            color: #00ffff;
            font-size: 18px;
        }

        a:hover {
            color: #ffffff;
        }

        button {
            background-color: #00a8a8;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #008080;
        }

        footer {
            background-color: #202830;
            padding: 15px;
            margin-top: 30px;
        }

        footer p {
            margin: 0;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Kali Linux</h1>
        <p>Learn Cybersecurity and Ethical Hacking</p>
    </header>

    <main>
        <h2>About Kali Linux</h2>
        <p>Kali Linux is a Linux distribution for security testing.</p>
        <p>It includes tools for penetration testing and digital forensics.</p>

        <h2>Getting Started</h2>
        <p>You can run Kali Linux inside Oracle VirtualBox.</p>

        <p>
            <a href="https://www.kali.org/get-kali/"
               target="_blank" rel="noopener noreferrer">
                Download Kali Linux
            </a>
        </p>

        <br>

        <button onclick="alert('Welcome to Kali Linux!')">
            Click Me
        </button>
    </main>

    <footer>
        <p>Created for Learning | Kali Linux Guide</p>
    </footer>
</body>
</html>
"""

components.html(
    html_code,
    height=750,
    scrolling=True
)
