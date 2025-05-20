"""Terminal utilities for colorful output."""

import time
import os

# ANSI color codes for terminal output
COLORS = {
    'GREEN': '\033[92m',
    'BLUE': '\033[94m',
    'YELLOW': '\033[93m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'END': '\033[0m'
}

def print_startup_banner():
    """Print a colorful startup banner."""
    startup_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{COLORS['BOLD']}{COLORS['CYAN']}======================================{COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['PURPLE']}   MATHLY API SERVER STARTING UP   {COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['CYAN']}======================================{COLORS['END']}")
    print(f"{COLORS['YELLOW']}Time: {startup_time}{COLORS['END']}")
    print(f"{COLORS['YELLOW']}Environment: {os.getenv('FLASK_ENV', 'development')}{COLORS['END']}")
    print(f"{COLORS['BOLD']}{COLORS['CYAN']}======================================{COLORS['END']}\n")

def print_routes(app):
    """Print all registered routes with color."""
    print(f"\n{COLORS['BOLD']}Registered Routes:{COLORS['END']}")
    for rule in app.url_map.iter_rules():
        print(f"{COLORS['GREEN']}• {rule.endpoint}{COLORS['END']}: {COLORS['BLUE']}{rule.methods}{COLORS['END']} -> {rule.rule}")
    
    print(f"\n{COLORS['BOLD']}{COLORS['PURPLE']}SERVER READY!{COLORS['END']}\n")