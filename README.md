# Via Scientific Documentation (vfdocs)

This repository contains the documentation for the Via Foundry platform. The documentation is written in Markdown and built using `mkdocs` with the `mkdocs-material` theme.

## Repository Structure

- **docs/**: Contains all the Markdown files for the documentation.
- **mkdocs.yml**: Configuration file for `mkdocs`.
- **.gitignore**: Specifies files to ignore in the repository.
- **README.md**: This file.

## Deployment

### Local Deployment

To deploy the documentation locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ViaScientific/vfdocs.git
   cd vfdocs
   ```

2. **Install dependencies**:
   Ensure you have Python and `pip` installed. Then, install `mkdocs` and `mkdocs-material`:
   ```bash
   pip install mkdocs mkdocs-material
   ```

3. **Serve the documentation locally**:
   ```bash
   mkdocs serve
   ```
   Open your browser and navigate to `http://127.0.0.1:8000` to view the documentation.

### Building for Production

To build the documentation for production, run:
```bash
mkdocs build
```
The built documentation will be located in the `site/` directory.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a Pull Request.

## Resources

For detailed information on writing and organizing documentation, refer to the [mkdocs documentation](https://www.mkdocs.org/).
