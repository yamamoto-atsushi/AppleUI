import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QShortcut, QKeySequence

from apple_style_ui import (
    AppleStyleWindow,
    AppleStyleLabel,
    AppleStyleLineEdit,
    AppleStyleTextEdit,
    AppleStyleButton,
    AppleStyleCheckBox,
    AppleStyleSwitch,
    AppleStyleSlider,
    AppleStyleRadioButton,
    AppleStyleComboBox,
    AppleStyleDateEdit,
    AppleStyleProgressBar,
    get_color, # Import the get_color function
)

class ComprehensiveSampleApp(AppleStyleWindow):
    def __init__(self):
        super().__init__("Comprehensive UI Showcase")

        # --- Main Layout ---
        # We will add widgets to self.layout directly using self.addContentWidget()

        # --- Title ---
        title_label = AppleStyleLabel("UI Component Showcase", font_size=24)
        title_label.setStyleSheet(title_label.styleSheet() + "font-weight: bold; padding-bottom: 15px;")
        self.addContentWidget(title_label)

        # --- Text Inputs ---
        name_label = AppleStyleLabel("Name (Drag & Drop a file path here):")
        self.addContentWidget(name_label)
        self.name_input = AppleStyleLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setToolTip("Your full name. You can also drag a file here to see its path.")
        self.addContentWidget(self.name_input)

        bio_label = AppleStyleLabel("Biography:")
        self.addContentWidget(bio_label)
        self.bio_edit = AppleStyleTextEdit()
        self.bio_edit.setPlaceholderText("Tell us about yourself...")
        self.bio_edit.setFixedHeight(80)
        self.bio_edit.setToolTip("A short biography.")
        self.addContentWidget(self.bio_edit)

        # --- Choices ---
        choices_label = AppleStyleLabel("Choices & Selections:", font_size=16)
        choices_label.setStyleSheet(choices_label.styleSheet() + "padding-top: 10px;")
        self.addContentWidget(choices_label)

        # Radio Buttons
        gender_layout_widget = QWidget()
        gender_layout = QHBoxLayout(gender_layout_widget)
        gender_layout.setContentsMargins(0,0,0,0)
        self.male_radio = AppleStyleRadioButton("Male")
        self.female_radio = AppleStyleRadioButton("Female")
        self.other_radio = AppleStyleRadioButton("Other")
        self.male_radio.setChecked(True)
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.other_radio)
        self.addContentWidget(gender_layout_widget)

        # ComboBox
        self.occupation_combo = AppleStyleComboBox()
        self.occupation_combo.addItems(["Student", "Developer", "Designer", "Manager", "Artist", "Other"])
        self.occupation_combo.setToolTip("Select your current occupation.")
        self.addContentWidget(self.occupation_combo)

        # DateEdit
        self.birthday_edit = AppleStyleDateEdit()
        self.birthday_edit.setDate(QDate(2000, 1, 1))
        self.birthday_edit.setToolTip("Select your birth date.")
        self.addContentWidget(self.birthday_edit)

        # --- Toggles & Controls ---
        controls_label = AppleStyleLabel("Toggles & Controls:", font_size=16)
        controls_label.setStyleSheet(controls_label.styleSheet() + "padding-top: 10px;")
        self.addContentWidget(controls_label)

        # CheckBox
        self.subscribe_checkbox = AppleStyleCheckBox("Subscribe to our amazing newsletter")
        self.subscribe_checkbox.setChecked(True)
        self.subscribe_checkbox.setToolTip("Stay updated with our news.")
        self.addContentWidget(self.subscribe_checkbox)

        # Switch
        self.darkMode_switch_label = AppleStyleLabel("Dark Mode (Visual Only - Use Theme Button):")
        self.addContentWidget(self.darkMode_switch_label)
        self.darkMode_switch = AppleStyleSwitch()
        self.darkMode_switch.setToolTip("This switch is a visual demo. Use 'Toggle Theme' button.")
        self.addContentWidget(self.darkMode_switch)

        # Slider
        self.volume_slider = AppleStyleSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(65)
        self.volume_slider.setToolTip("Adjust volume level.")
        self.addContentWidget(self.volume_slider)

        # --- Progress & Status ---
        status_label = AppleStyleLabel("Progress & Status:", font_size=16)
        status_label.setStyleSheet(status_label.styleSheet() + "padding-top: 10px;")
        self.addContentWidget(status_label)

        self.progress_bar = AppleStyleProgressBar()
        self.progress_bar.setToolTip("Shows current task progress.")
        self.addContentWidget(self.progress_bar)

        # Timer to simulate progress
        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self._update_progress)
        self.progress_value = 0

        # Message Label (already part of AppleStyleWindow, we'll use it via show_message)
        # self.addContentWidget(self.message_label) # Added in AppleStyleWindow

        # --- Action Buttons ---
        actions_label = AppleStyleLabel("Actions:", font_size=16)
        actions_label.setStyleSheet(actions_label.styleSheet() + "padding-top: 10px;")
        self.addContentWidget(actions_label)

        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.setContentsMargins(0,0,0,0)

        self.theme_button = AppleStyleButton("Toggle Theme")
        self.theme_button.setToolTip("Switch between light and dark UI themes.")
        self.theme_button.clicked.connect(self._toggle_theme_and_buttons_style)
        buttons_layout.addWidget(self.theme_button)

        self.help_button = AppleStyleButton("Help")
        self.help_button.setToolTip("Show application help.")
        self.help_button.clicked.connect(self._show_help_dialog)
        buttons_layout.addWidget(self.help_button)

        buttons_layout.addStretch()

        self.submit_button = AppleStyleButton("Submit Data")
        self.submit_button.setToolTip("Submit the entered data (Ctrl+S / Cmd+S).")
        self.submit_button.clicked.connect(self._submit_data)
        # Keyboard Shortcut for Submit
        save_shortcut = QShortcut(QKeySequence.StandardKey.Save, self)
        save_shortcut.activated.connect(self._submit_data)
        buttons_layout.addWidget(self.submit_button)

        self.addContentWidget(buttons_widget)

        # Apply initial styles to secondary buttons
        self._style_secondary_button(self.theme_button)
        self._style_secondary_button(self.help_button)

        # Add message label to the layout (it's created in AppleStyleWindow)
        self.layout.addWidget(self.message_label)
        self.addStretch() # Ensure content is pushed up, and message label is above stretch

        # Start progress simulation
        self.progress_timer.start(100) # Update every 100ms

    def _update_progress(self):
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        self.progress_bar.setValue(self.progress_value)

    def _style_secondary_button(self, button):
        button._update_colors() # Ensure base colors are from current theme
        button._default_bg_color = get_color("separator")
        button._hover_bg_color = get_color("disabled_background")
        button._pressed_bg_color = get_color("input_border")
        button._text_color = get_color("text_primary")
        button._current_bg_color = button._default_bg_color
        button._apply_style()

    def _toggle_theme_and_buttons_style(self):
        current_theme_name = self.current_theme
        if current_theme_name == "light":
            self.set_theme("dark")
        else:
            self.set_theme("light")
        # Re-style secondary buttons after theme change
        self._style_secondary_button(self.theme_button)
        self._style_secondary_button(self.help_button)

    def _show_help_dialog(self):
        QMessageBox.information(self, "Help",
                                "This application showcases various UI components styled in an Apple-like fashion. "
                                "Explore different controls and features like theme toggling and settings persistence.")

    def _submit_data(self):
        name = self.name_input.text()
        bio = self.bio_edit.toPlainText()
        gender = "Male" if self.male_radio.isChecked() else "Female" if self.female_radio.isChecked() else "Other"
        occupation = self.occupation_combo.currentText()
        birthday = self.birthday_edit.date().toString(Qt.DateFormat.ISODate)
        subscribed = "Yes" if self.subscribe_checkbox.isChecked() else "No"
        volume = self.volume_slider.value()

        summary = (f"--- Submitted Data ---\n"
                   f"Name: {name}\nBio: {bio[:30]}...\nGender: {gender}\n"
                   f"Occupation: {occupation}\nBirthday: {birthday}\n"
                   f"Subscribed: {subscribed}\nVolume: {volume}")
        print(summary)
        self.show_message(f"Data for '{name}' submitted!", duration_ms=3000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Ensure settings are initialized for the application
    QApplication.setOrganizationName("MyCompany") # For QSettings
    QApplication.setApplicationName("ComprehensiveAppleUIApp") # For QSettings

    main_app = ComprehensiveSampleApp()
    main_app.show()
    sys.exit(app.exec())