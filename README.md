# Ramer-Douglas-Peucker Algorithm

Implementation of Ramer-Douglas-Peucker Algorithm on Rust with Python bindings.
Supports passing multiple lines (the line is [[x, y], [x, y]...]), each line is processed in a separate os-thread.

The number of threads is bound to a number of logical CPUs
