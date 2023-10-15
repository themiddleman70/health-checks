#!/usr/bin/env python

import os
import sys

def check_reboot():
	"""Returns True if the computer has a pending reoboot."""
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print("Pending reboot.")
		sys.exit(1)
	print("Everything okay.")
	sys.exit(0)

main()
