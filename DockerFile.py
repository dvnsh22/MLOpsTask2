{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import os\n",
    "def check_if_string_in_file(file_name, string_to_search):\n",
    "    with open(file_name, 'r') as read_obj:\n",
    "        for line in read_obj:\n",
    "            if string_to_search in line:\n",
    "                return True\n",
    "    return False\n",
    "\n",
    "# Searching For PHP\n",
    "if check_if_string_in_file('Main.php', '<?php'):\n",
    "    os.system('echo \"Yes, string found\"')\n",
    "    os.system('sudo docker -divt /root/MLOpsTask2:/root/ --name Docker_OS httpd')\n",
    "\n",
    "else:\n",
    "    os.system('echo \"Yes, string found\"')\n",
    "    os.system('sudo docker -divt /root/MLOpsTask2:/root/ --name Docker_OS docker1')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
