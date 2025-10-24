import os, argparse

# Option parser
parser = argparse.ArgumentParser(description="MC/DC Verification - Analytical")
parser.add_argument("--srun", type=int, default=0)
parser.add_argument("--mpiexec", type=int, default=0)
parser.add_argument("--mpirun", type=int, default=0)
args, unargs = parser.parse_known_args()

# Get the MPI option
mpi_option = ""
if args.srun > 0 or args.mpiexec > 0 or args.mpirun > 0:
    if args.srun > 1:
        mpi_option = f"--srun {args.srun}"
    elif args.mpiexec > 1:
        mpi_option = f"--mpiexec {args.mpiexec}"
    elif args.mpirun > 1:
        mpi_option = f"--mpirun {args.mpirun}"

# Analytical verification - Suite A
os.chdir("verification/analytical/suite_A")
os.system(f"python run.py {mpi_option}")
os.chdir("../../../")
