# IMAP Concourse Resource

A Concourse resource that checks for new emails from an IMAP server and outputs their contents to a file.

## Source Configuration

```yaml
resource_types:
- name: email
  type: docker-image
  source:
    repository: your-docker-hub-username/imap-concourse-resource

resources:
- name: my-email
  type: email
  source:
    server: imap.mail.yahoo.com
    user: ((email-user))
    password: ((email-password))
    folder: INBOX
    email_body_only: false

```

* `server`: The address of the IMAP server (required)
* `user`: The username to log in to the server (required)
* `password`: The password to log in to the server (required)
* `folder`: The folder to check for new emails (required)
* `email_body_only`: Set to `true` to only output the body of the email instead of the entire MIME email (optional, defaults to `false`)
* `check_return_unread_only`: Set to `true` to only return unread in the versions (optional, defaults to `true`)
* `email_limit`: The maximum number of emails to return in the versions (optional, defaults to `5`)
* `subject_glob`: A glob pattern to match against the subject of the email (optional, defaults to `*`)

## Behavior

### `check` for new emails from the IMAP server

The `check` script connects to the IMAP server, checks the specified folder for new (unread) emails, and returns a list of new email IDs and their timestamps. Each new email is represented by a version.

### `in`: Fetch an email from the IMAP server

The `in` script takes a version produced by the check script, connects to the IMAP server, fetches the email 
corresponding to the version, and writes the contents of the email to a file named `email.txt`. It then returns the ID of the fetched email.

In addition to the `email.txt` file, the subject is written to a file named `subject.txt` and the sender is written to a file named `sender.txt`.


#### Parameters

None

## Example

```yaml
jobs:
- name: do-something-with-email
  plan:
  - get: my-email
    trigger: true
  - task: do-something
    config:
      platform: linux
      image_resource:
        type: docker-image
        source: {repository: alpine}
      run:
        path: /bin/sh
        args:
        - -c
        - |
          echo "New email received!"
          cat my-email/email.txt
    inputs:
    - name: my-email

```
