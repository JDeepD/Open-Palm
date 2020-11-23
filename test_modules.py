# noqa

import unittest


class TestAnalyse(unittest.TestCase):

    def test_modules(self):
        import tkinter
        from tkinter import ttk
        from tkinter.filedialog import askopenfilename, asksaveasfilename
        import tkinter.messagebox
        from functools import wraps
        from importlib import reload
        from os import path, mkdir
        import sqlite3
        import smtplib
        from email.mime.text import MIMEText
        import csv


if __name__ == "__main__":
    unittest.main()
