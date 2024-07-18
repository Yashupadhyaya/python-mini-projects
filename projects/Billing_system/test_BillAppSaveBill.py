# ********RoostGPT********
"""
Test generated by RoostGPT for test test-python using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=save_bill_420ec392d0
ROOST_METHOD_SIG_HASH=save_bill_4312133209


Scenario 1: Test to check if the bill is saved when the user chooses to save it.
Details:
  TestName: test_save_bill_yes
  Description: This test will verify if the bill data is saved into a file when the user chooses to do so.
Execution:
  Arrange: Initialize the billing application with required data.
  Act: Call the save_bill method and simulate a 'yes' response to the messagebox.
  Assert: Check if the file is created in the expected directory with the expected bill number, and the content of the file matches the expected bill data.
Validation:
  This test is important to ensure that the bill data is correctly saved when the user wants to save it. The expected result is that a file with the bill number is created in the "bills" directory and the content of the file matches the bill data.

Scenario 2: Test to check if the bill is not saved when the user chooses not to save it.
Details:
  TestName: test_save_bill_no
  Description: This test will verify if the bill data is not saved into a file when the user chooses not to do so.
Execution:
  Arrange: Initialize the billing application with required data.
  Act: Call the save_bill method and simulate a 'no' response to the messagebox.
  Assert: Check if the file is not created in the expected directory with the expected bill number.
Validation:
  This test is important to ensure that the bill data is not saved when the user does not want to save it. The expected result is that no file is created in the "bills" directory.

Scenario 3: Test to check if the bill is saved with correct content when the user chooses to save it.
Details:
  TestName: test_save_bill_content
  Description: This test will verify if the bill data is correctly written into the file when the user chooses to save it.
Execution:
  Arrange: Initialize the billing application with required data.
  Act: Call the save_bill method and simulate a 'yes' response to the messagebox.
  Assert: Check if the content of the file matches the expected bill data.
Validation:
  This test is important to ensure that the bill data is correctly written into the file when the user wants to save it. The expected result is that the content of the file matches the bill data.

Scenario 4: Test to check if the correct success message is displayed when the user chooses to save the bill.
Details:
  TestName: test_save_bill_success_message
  Description: This test will verify if the correct success message is displayed when the user chooses to save the bill.
Execution:
  Arrange: Initialize the billing application with required data.
  Act: Call the save_bill method and simulate a 'yes' response to the messagebox.
  Assert: Check if the correct success message is displayed.
Validation:
  This test is important to ensure that the user is correctly informed when the bill is successfully saved. The expected result is that the correct success message is displayed.
"""

# ********RoostGPT********
import pytest
import os
from tkinter import messagebox
from unittest.mock import Mock, patch
from Billing_system.biling_system import Bill_App

class Test_BillAppSaveBill:

    @pytest.fixture
    def mock_root(self):
        return Mock()

    @pytest.fixture
    def bill_app(self, mock_root):
        return Bill_App(mock_root)

    @patch.object(Bill_App, 'bill_area')
    def test_save_bill_yes(self, mock_bill_area, bill_app):
        bill_app.txtarea.get = Mock(return_value="Bill Data")
        with patch.object(messagebox, 'askyesno', return_value=True):
            with patch.object(messagebox, 'showinfo') as mock_showinfo:
                bill_app.save_bill()
        mock_bill_area.assert_called_once()
        mock_showinfo.assert_called_once_with("Saved", f"Bill no:{bill_app.bill_no.get()} Saved Successfully")
        file_path = f"bills/{bill_app.bill_no.get()}.txt"
        assert os.path.exists(file_path)
        with open(file_path, "r") as f:
            assert f.read() == "Bill Data"
        os.remove(file_path)

    @patch.object(Bill_App, 'bill_area')
    def test_save_bill_no(self, mock_bill_area, bill_app):
        with patch.object(messagebox, 'askyesno', return_value=False):
            bill_app.save_bill()
        mock_bill_area.assert_not_called()
        file_path = f"bills/{bill_app.bill_no.get()}.txt"
        assert not os.path.exists(file_path)

    @patch.object(Bill_App, 'bill_area')
    def test_save_bill_content(self, mock_bill_area, bill_app):
        bill_app.txtarea.get = Mock(return_value="Bill Data")
        with patch.object(messagebox, 'askyesno', return_value=True):
            bill_app.save_bill()
        mock_bill_area.assert_called_once()
        file_path = f"bills/{bill_app.bill_no.get()}.txt"
        assert os.path.exists(file_path)
        with open(file_path, "r") as f:
            assert f.read() == "Bill Data"
        os.remove(file_path)

    @patch.object(Bill_App, 'bill_area')
    def test_save_bill_success_message(self, mock_bill_area, bill_app):
        with patch.object(messagebox, 'askyesno', return_value=True):
            with patch.object(messagebox, 'showinfo') as mock_showinfo:
                bill_app.save_bill()
        mock_showinfo.assert_called_once_with("Saved", f"Bill no:{bill_app.bill_no.get()} Saved Successfully")
