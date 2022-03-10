"""
Script to detect whether it is running on top of a proprietary OS or not.

It will display an error message in the available UI framework, if it detected a proprietary OS.
"""
__maintainer__ = "zer0-x"
__license__ = "GPL-3.0"
__version__ = "0.1"


_WINDOW_TITLE = "Proprietary OS Error!"
_TEXT_TITLE = "Your operating system has been detected as proprietary!"
_INFO_TEXT = (
    "The FOSS-Shield detected a proprietary software running as your OS. "
    + "The operation has been aborted by FOSS-Shield in order to maintain your security "
    + "and privacy from criminals' interference. To solve this error, you can go to "
    + '<a href="https://www.fsf.org/">fsf.org</a>.'
)
_DETAILED_TEXT = (
    "That means that your OS is affiliated with a monopoly criminal group of "
    + "the United States of America and it violates your security and privacy. "
    + "They store your data in their servers, do suspicious and criminal things with them, "
    + "and share them with the NSA, CIA, FPI,all the countries participating with them in this "
    + "process, and they link your activities collected by other criminal groups. "
    + "Therefor, this operation was aborted from running by The FOSS Shield."
    + "You need to use a private and secure OS in order to run this software."
    + "All this for the purpose of protecting you and your data."
)
_SIMPLE_MSG = (
    "The FOSS-Shield detected a proprietary software running as your operating system. "
    + "Please use a Free and Open-Source Software to run this program. "
    + "Learn more about free-software at fsf.org"
)
_SIMPLE_MSG_MAEKUP = (
    "The FOSS-Shield detected a proprietary software running as your operating system. "
    + "Please use a Free and Open-Source Software to run this program. "
    + 'Learn more about free software at <a href="https://www.fsf.org/">fsf.org</a>'
)


class ProprietarySoftwareError(Exception):
    """Error to be raised when detecting a proprietary operating system."""

    pass


def _qt5():
    try:
        from PyQt5 import QtWidgets
    except (
        ModuleNotFoundError,
        ImportError,
    ):
        return False
    else:
        app = QtWidgets.QApplication([])

        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle(_WINDOW_TITLE)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(_TEXT_TITLE)
        msg.setInformativeText(_INFO_TEXT)
        msg.setDetailedText(_DETAILED_TEXT)

        msg.exec_()

        return True


def _qt6():
    try:
        try:
            from PyQt6 import QtWidgets
        except Exception:
            from PySide6 import QtWidgets
    except Exception:
        return False
    else:
        app = QtWidgets.QApplication([])

        msg = QtWidgets.QMessageBox()

        msg.setWindowTitle(_WINDOW_TITLE)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setText(_TEXT_TITLE)
        msg.setInformativeText(_INFO_TEXT)
        msg.setDetailedText(_DETAILED_TEXT)

        msg.exec()

        return True


def _gtk3():
    try:
        import gi

        gi.require_version("Gtk", "3.0")
        from gi.repository import Gtk
    except Exception:
        return False
    else:
        dialog = Gtk.MessageDialog(
            parent=None,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CLOSE,
        )
        dialog.set_title(_WINDOW_TITLE)
        dialog.set_markup(_SIMPLE_MSG_MAEKUP)
        dialog.show()
        dialog.run()
        dialog.destroy()


def _tkinter():
    try:
        from tkinter import messagebox
    except Exception:
        return False
    else:
        messagebox.showerror(_WINDOW_TITLE, f"{_SIMPLE_MSG}")


# _qt5, _qt6, _gtk3, _tkinter
_functions = [_qt5, _qt6, _gtk3, _tkinter]
_ALLOWED_PLATFORMS = ["Linux"]


def run() -> None:
    """Run the proprietary software detector."""
    if __import__("platform").system() in _ALLOWED_PLATFORMS:
        for _function in _functions:
            # When a message is displayed the loop will break.
            if _function():
                break
        # For error message in the CLI.
        raise ProprietarySoftwareError(_SIMPLE_MSG)
    return None


if __name__ == "__main__":
    run()
