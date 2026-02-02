# TASK 3: Bug Reporting

## Bug #1: Invalid Login UI Alignment
* [cite_start]**Summary:** Error message "Invalid credentials" overlaps with the login button on mobile view. [cite: 36]
* [cite_start]**Steps to Reproduce:** [cite: 37]
  1. Open OrangeHRM login page.
  2. Enter invalid credentials.
  3. Resize browser to mobile width (375px).
* [cite_start]**Expected Result:** Error message should be centered and not overlap. [cite: 38]
* [cite_start]**Actual Result:** Text overlaps the button, making it hard to read. [cite: 39]
* **Severity:** Minor | [cite_start]**Priority:** Low [cite: 40]

## Bug #2: Password Reset Link Security
* [cite_start]**Summary:** "Forgot your password" link remains active after the password has already been changed. [cite: 36]
* [cite_start]**Steps to Reproduce:** [cite: 37]
  1. Request a password reset link.
  2. Use the link to change the password once.
  3. Click the same link again.
* [cite_start]**Expected Result:** Link should expire after one use. [cite: 38]
* [cite_start]**Actual Result:** Link allows multiple password changes. [cite: 39]
* **Severity:** Critical | [cite_start]**Priority:** High [cite: 40]

## Bug #3: Missing Mandatory Field Validation
* [cite_start]**Summary:** System allows saving a new employee with a blank Employee ID. [cite: 36]
* [cite_start]**Steps to Reproduce:** [cite: 37]
  1. Go to PIM > Add Employee.
  2. Enter First/Last name but delete the auto-filled ID.
  3. Click Save.
* [cite_start]**Expected Result:** "Required" error message should appear for ID field. [cite: 38]
* [cite_start]**Actual Result:** Employee is saved without an ID. [cite: 39]
* **Severity:** Major | [cite_start]**Priority:** Medium [cite: 40]

## Bug #4: Invalid File Format Upload
* [cite_start]**Summary:** System accepts .pdf files in the Profile Picture upload field. [cite: 36]
* [cite_start]**Steps to Reproduce:** [cite: 37]
  1. Go to My Info module.
  2. Click the profile picture to upload a new one.
  3. Select a PDF file.
* [cite_start]**Expected Result:** Only image formats (JPG/PNG) should be accepted. [cite: 38]
* [cite_start]**Actual Result:** PDF is uploaded and displays as a broken image. [cite: 39]
* **Severity:** Minor | [cite_start]**Priority:** Low [cite: 40]

## Bug #5: Session Timeout Redirection
* [cite_start]**Summary:** Session expiration leads to a 404 error instead of the Login page. [cite: 36]
* [cite_start]**Steps to Reproduce:** [cite: 37]
  1. Stay inactive until the session expires.
  2. Click on the "Admin" menu.
* [cite_start]**Expected Result:** System should redirect to the Login screen. [cite: 38]
* [cite_start]**Actual Result:** System displays a "404 Page Not Found" error. [cite: 39]
* **Severity:** Major | [cite_start]**Priority:** Medium [cite: 40]