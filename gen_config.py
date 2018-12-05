#!/usr/bin/python
# -*- coding: utf-8 -*-
import locale
import gen_events as events

# Year to generate for
year = 2019

# True if the week starts on Monday (European convention), False if it starts on Sunday.
week_starts_on_Monday = True

# What paper size should be output?
paper_size = 'a5paper'
# Use paper_size = 'paperheight=8.5in,paperwidth=5.5in' for half letter,
# paper_size = 'paperheight=9in,paperwidth=6in' for lulu hardcover.

# Locale -- uncomment one only, use utf-8 encoding ONLY
#
#locale.setlocale(locale.LC_ALL, 'en_AU.utf-8')      # Australia
locale.setlocale(locale.LC_ALL, 'en_GB.utf-8')      # Great Britain
#locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')      # France
#locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')      # Deuchland
#locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')      # Espaniol

# Define "Week" and "Notes" words, being used in the Weekly Planner
Week_locale = 'Week'
HowGo_locale = 'How did it go?'
Notes_locale = 'Notes'
Week_Goals_locale = 'Week Goals'
Physical_Activity_locale = 'Exercise'

# What events should be built in to the calendar?
# Pass in the year, month, day, event name, and True if the day is a holiday
# and should be greyed out on the calendar
events.add_event(year, 1, 1, "New Year's Day", True)
events.add_event(year + 1, 1, 1, "New Year's Day", True)


# Numbers of 'extra' pages
# The standard pages (calendars, planners, OKRs, etc) take up 147 pages.
# How many and what other pages should be included?
num_dots_pages = 10
num_triangular_dots_pages = 10
num_graph_pages = 6
num_blank_pages = 10
num_smartphone_wireframe_pages = 4
enable_coloring_pages = True # total of 9 pages
enable_git_cheat_sheet = False # A simple list of common git commands
enable_constants_page = True # some scientific constants
enable_ascii_page = True # an ascii table
enable_numbers_page = True # Country population / latency numbers
