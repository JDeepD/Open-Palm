
try:
    import MainUI  # noqa pylint: disable=all
except ImportError:
    from src import MainUI


window = MainUI.Openpalm()
window.title('OpenPalm')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)
window.mainloop()