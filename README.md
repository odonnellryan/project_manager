# project_manager

Django project, will be custom project management software.

Spec:

0) A way to create projects
    - break projects down into work items
        - those work items into smaller work items
            - split feature to break items up, creates multiple children each time
    - assign members to projects, projects to members
    
1) A way to layout projects visibly
    - view and document work items and child items
    - close old projects
    - assign people to projects
    - based on the estimate for each work item the project has a goal-date

2) work items
    - are the bits of a project that need to be completed
    - are up to the client, but should be as small as possible
    - can contain information, have multiple people working on them
    - can have children and parent items
    - can be grouped based on releases (parent work items)
    - will include a time estimate for each assigned member

django admin: odonnellr // pm_user