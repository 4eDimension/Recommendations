# General recommendations

<u>Recommended:</u>

- Use a supported line, of your choice:

    - The Feature Release line: 20 Rx

    - The Long Term Support Release line: 20.x

- Deploy the most recent version of the line you have chosen:

    - Feature Release line:

        - A new R version is available every 3 months containing new
      features

        - 2 HotFixes are available monthly for the current R version
      containing bug fixes preventing its use in deployment (you will
      have to wait for the next R version for the other bugs)

    - LTS Release line:

        - A new major version is available every 18 months containing the
      features of the 6 previous R versions

        - Minor releases and HotFixes are regularly available for the
      current major LTS release containing bug fixes

- You can use the Feature Release line in development to benefit from
  important implementations offered by 4D as soon as possible

- Develop in project mode

- Use repository and source control tools for collaborative development
  but also to manage your different development and deployment branches

- Use UUID fields for primary keys

- Draw links between tables and name your links

- Do not use the \"MODIFY SELECTION\" command

- Use objects

- Use listboxes for lists

- Use only object names
