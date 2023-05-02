{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import xml.etree.ElementTree as ET\n",
    "import csv\n",
    "\n",
    "folder_path = r\"C:\\Users\\Dominic's PC\\OneDrive\\Documents\\Cambridge\\MPhil DH\\Dissertation\\Coding\\Data cleaning\\Test 1\\output\"\n",
    "\n",
    "def extract_transcript_notes(root):\n",
    "    notes = \"\"\n",
    "    for note in root.iter('note'):\n",
    "        if 'transcript' in note.text:\n",
    "            for p in note.iter('p'):\n",
    "                notes += p.text\n",
    "    return notes\n",
    "\n",
    "# Create a new spreadsheet\n",
    "with open('output.csv', mode='w', newline='') as file:\n",
    "    writer = csv.writer(file)\n",
    "    writer.writerow(['File Name', 'unitdate normal', 'Note'])\n",
    "    \n",
    "    # Sort the xml files in the specified folder by file name\n",
    "    xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]\n",
    "    xml_files.sort()\n",
    "    \n",
    "    # Loop through all xml files in the specified folder\n",
    "    for filename in xml_files:\n",
    "        file_path = os.path.join(folder_path, filename)\n",
    "        tree = ET.parse(file_path)\n",
    "        root = tree.getroot()\n",
    "        \n",
    "        # Extract the \"unitdate normal\" value\n",
    "        unitdate_normal = \"\"\n",
    "        unitdate_element = root.find('.//unitdate[@normal]')\n",
    "        if unitdate_element is not None:\n",
    "            unitdate_normal = unitdate_element.attrib['normal']\n",
    "        \n",
    "        # Write the file name, \"unitdate normal\" value, and note to the spreadsheet\n",
    "        writer.writerow([filename, unitdate_normal])"
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
   "version": "3.8.10"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "6615c45bc055f43bb64b4ffa69373302ac6e7e150b5d86df7bc2c51bcc17dd09"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
