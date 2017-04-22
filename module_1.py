import logging
import module_2

if __name__ == "__main__":
	logging.basicConfig(filename="multiple_logs.log", level=logging.INFO)
	logging.info("info 1 module_1")
	module_2.test()
	logging.info("info 2 module_1")



# --------- FILE OUTPUT ---------
# INFO:root:info 1 module_1
# INFO:root:module 2
# INFO:root:info 2 module_1
# ----------------------------------