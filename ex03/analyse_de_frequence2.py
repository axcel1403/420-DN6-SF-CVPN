# AnalyseDeFrequence2.py

secret = """LRVMNIR BPR SUMVBWVR JX BPR LMIWV YJERYRKBI JX QMBM WI
BPR XJVNI MKD YMIBRUT JX IRHX WI BPR RIIRKVR JX
YMBINLMTMIPW UTN QMUMBR DJ W IPMHH BUT BJ RHNVWDMBR BPR
YJERYRKBI JX BPR QMBM MVVJUDWKO BJ YT WKBRUSURBMBWJK
LMIRD JK XJUBT TRMUI JX IBNDT
WB WI KJB MK RMIT BMIQ BJ RASHMWK RMVP YJERYRKB MKD WBI
IWOKWXWVMKVR MKD IJYR YNIB URYMWK NKRASHMWKRD BJ OWER M
VJYSHRBR RASHMKMBWJK JKR CJNHD PMER BJ LR FNMHWXWRD MKD
WKISWURD BJ INVP MK RABRKB BPMB PR VJNHD URMVP BPR IBMBR
JX RKHWOPBRKRD YWKD VMSMLHR JX URVJOKWGWKO IJNKDHRII
IJNKD MKD IPMSRHRII IPMSR W DJ KJB DRRY YTIRHX BPR XWKMH
MNBPJUWBT LNB YT RASRUWRKVR CWBP QMBM PMI HRXB KJ DJNLB
BPMB BPR XJHHJCWKO WI BPR SUJSRU MSSHWVMBWJK MKD
WKBRUSURBMBWJK W JXXRU YT BPRJUWRI WK BPR PJSR BPMB BPR
RIIRKVR JX JQWKMCMK QMUMBR CWHH URYMWK WKBMVB
"""

class Attaque:
	def	__init__(self):
		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.freq = {}
	
	def	calculate_freq(self, secret):
		for c in self.alphabet:
			self.freq[c] = 0
		
		letter_count = 0

		for c in secret:
			if c in self.freq:
				self.freq[c] += 1
				letter_count += 1

		for c in self.freq:
			self.freq[c] = round(self.freq[c]/letter_count, 4)

	def	print_freq(self):
		new_line_count = 0
		
		for c in self.freq:
			print(c, ":", self.freq[c], " ", end='')
			if new_line_count % 3 == 2:
				print()
			new_line_count += 1

pirate = Attaque()
pirate.calculate_freq(secret)
pirate.print_freq()
