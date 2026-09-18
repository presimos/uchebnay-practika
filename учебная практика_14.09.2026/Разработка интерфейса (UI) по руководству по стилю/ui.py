import tkinter as tk
from pathlib import Path
from tkinter import ttk

from models import Partner


BACKGROUND = "#FFFFFF"
BORDER = "#8B8B8B"
TEXT = "#1F1F1F"


class PartnerCrmApp(tk.Tk):
    def __init__(self, partners: list[Partner], resources_dir: Path) -> None:
        super().__init__()
        self.title("CRM: Список партнеров и скидок")
        self.configure(background=BACKGROUND)
        self.geometry("760x560")
        self.minsize(620, 420)
        self._logo = tk.PhotoImage(file=resources_dir / "logo.png").subsample(18, 18)
        self._icon = tk.PhotoImage(file=resources_dir / "app_icon.png").subsample(24, 24)
        self.iconphoto(True, self._icon)
        self._create_header()
        self._create_cards(partners)

    def _create_header(self) -> None:
        header = ttk.Frame(self, padding=(28, 20, 28, 12))
        header.pack(fill=tk.X)
        logo = ttk.Label(header, image=self._logo)
        logo.pack(side=tk.LEFT)
        title = ttk.Label(
            header,
            text="CRM: Список партнеров и скидок",
            font=("Arial", 16, "bold"),
        )
        title.pack(side=tk.LEFT, padx=(12, 0))

    def _create_cards(self, partners: list[Partner]) -> None:
        canvas = tk.Canvas(
            self,
            background=BACKGROUND,
            highlightthickness=0,
        )
        scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICAL,
            command=canvas.yview,
        )
        content = ttk.Frame(
            canvas,
            padding=(28, 0, 28, 28),
        )

        content.bind(
            "<Configure>",
            lambda event: canvas.configure(
                scrollregion=canvas.bbox("all"),
            ),
        )

        canvas_window = canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw",
        )

        def update_content_width(event: tk.Event) -> None:
            canvas.itemconfigure(
                canvas_window,
                width=event.width,
            )

        canvas.bind("<Configure>", update_content_width)

        canvas.configure(
            yscrollcommand=scrollbar.set,
        )

        canvas.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
        )
        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y,
        )

        for partner in partners:
            self._create_card(content, partner)

    def _create_card(self, parent: ttk.Frame, partner: Partner) -> None:
        card = tk.Frame(
            parent,
            background=BACKGROUND,
            highlightbackground=BORDER,
            highlightthickness=1,
            padx=24,
            pady=14,
        )
        card.pack(fill=tk.X, pady=(0, 14))
        details = tk.Frame(card, background=BACKGROUND)
        details.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Label(
            details,
            text=f"Партнёр | {partner.company_name}",
            background=BACKGROUND,
            foreground=TEXT,
            font=("Arial", 12),
            anchor="w",
        ).pack(fill=tk.X)
        tk.Label(
            details,
            text=f"Контакт: {partner.contact_email}",
            background=BACKGROUND,
            foreground=TEXT,
            font=("Arial", 10),
            anchor="w",
        ).pack(fill=tk.X)
        phone = partner.phone or "не указан"
        tk.Label(
            details,
            text=f"Телефон: {phone}",
            background=BACKGROUND,
            foreground=TEXT,
            font=("Arial", 10),
            anchor="w",
        ).pack(fill=tk.X)
        rating = "не указан" if partner.rating is None else str(partner.rating)
        tk.Label(
            details,
            text=f"Рейтинг: {rating}",
            background=BACKGROUND,
            foreground=TEXT,
            font=("Arial", 10),
            anchor="w",
        ).pack(fill=tk.X)
        tk.Label(
            card,
            text=f"{partner.discount}%",
            background=BACKGROUND,
            foreground=TEXT,
            font=("Arial", 14),
        ).pack(side=tk.RIGHT, anchor=tk.N)
