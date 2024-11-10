# 99DaysWithCPC - Machine Learning

from tkinter import *
import calendar
from datetime import datetime

# Custom color scheme
COLORS = {
    "primary": "#4A90E2",  # Blue
    "secondary": "#F5F7FA",  # Light Gray
    "accent": "#50C878",  # Emerald Green
    "text": "#2C3E50",  # Dark Blue Gray
    "highlight": "#E74C3C",  # Coral Red
}


class CalendarApp:
    def __init__(self):
        self.setup_main_window()
        self.create_widgets()

    def setup_main_window(self):
        """Initialize the main application window with basic settings"""
        self.root = Tk()
        self.root.title("Modern Calendar")
        self.root.geometry("550x700")
        self.root.configure(bg=COLORS["secondary"])

        # Center the window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 550) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"550x700+{x}+{y}")

    def create_widgets(self):
        """Create and arrange all widgets in the main window"""
        # Title Frame
        title_frame = Frame(self.root, bg=COLORS["primary"], pady=15)
        title_frame.pack(fill=X)

        # App Title
        title = Label(
            title_frame,
            text="Calendar App",
            font=("Helvetica", 24, "bold"),
            bg=COLORS["primary"],
            fg="white",
        )
        title.pack()

        # Current Date Display
        current_date = datetime.now().strftime("%B %d, %Y")
        date_label = Label(
            title_frame,
            text=current_date,
            font=("Helvetica", 12),
            bg=COLORS["primary"],
            fg="white",
        )
        date_label.pack()

        # Year Input Frame
        input_frame = Frame(self.root, bg=COLORS["secondary"], pady=20)
        input_frame.pack(fill=X)

        # Year Label and Entry
        year_label = Label(
            input_frame,
            text="Enter Year:",
            font=("Helvetica", 14),
            bg=COLORS["secondary"],
            fg=COLORS["text"],
        )
        year_label.pack()

        self.year_entry = Entry(
            input_frame, font=("Helvetica", 14), justify="center", width=10
        )
        self.year_entry.insert(0, str(datetime.now().year))
        self.year_entry.pack(pady=5)

        # Show Calendar Button
        show_button = Button(
            input_frame,
            text="Show Calendar",
            font=("Helvetica", 12, "bold"),
            bg=COLORS["accent"],
            fg="white",
            command=self.show_calendar,
            padx=20,
            pady=5,
            relief=FLAT,
        )
        show_button.pack(pady=10)

        # Calendar Display Frame
        self.calendar_frame = Frame(self.root, bg=COLORS["secondary"])
        self.calendar_frame.pack(expand=True, fill=BOTH, padx=20)

    def show_calendar(self):
        """Display the calendar for the specified year"""
        # Clear previous calendar if any
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        try:
            # Get year from entry
            year = int(self.year_entry.get())

            # Create calendar instance with Monday as first day of week
            cal = calendar.TextCalendar(calendar.MONDAY)

            # Create monthly calendars
            for month in range(1, 13):
                # Month frame
                month_frame = Frame(
                    self.calendar_frame, bg=COLORS["secondary"], padx=10, pady=5
                )
                month_frame.grid(
                    row=(month - 1) // 3, column=(month - 1) % 3, sticky="nsew"
                )

                # Month title
                month_name = calendar.month_name[month]
                Label(
                    month_frame,
                    text=month_name,
                    font=("Helvetica", 10, "bold"),
                    bg=COLORS["primary"],
                    fg="white",
                    padx=5,
                    pady=2,
                ).pack(fill=X)

                # Format calendar text
                month_cal = cal.formatmonth(year, month)

                # Display calendar with custom font and colors
                cal_label = Label(
                    month_frame,
                    text=month_cal,
                    font=("Courier", 8, "bold"),
                    bg=COLORS["secondary"],
                    fg=COLORS["text"],
                    justify=LEFT,
                )
                cal_label.pack(pady=5)

        except ValueError:
            # Show error if invalid year entered
            error_label = Label(
                self.calendar_frame,
                text="Please enter a valid year!",
                font=("Helvetica", 12),
                fg=COLORS["highlight"],
                bg=COLORS["secondary"],
            )
            error_label.pack(pady=20)


if __name__ == "__main__":
    app = CalendarApp()
    app.root.mainloop()
