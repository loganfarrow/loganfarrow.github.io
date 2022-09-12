vcf_file = "/Users/loganfarrow/Desktop/gnomad.exomes.r2.1.1.sites.7.vcf.bgz"
def read_vcf(vcf_file):
    """
    Read a vcf file to a dict of lists.

    :param str vcf_file: Path to a vcf file.
    :return: dict of lists of vcf records
    :rtype: dict
    """
    vcf_dict = []
    with open(vcf_file, 'r') as invcf:
        for line in invcf:
            if line.startswith('#'):
                continue
            line = line.strip().split()
            vcf_dict.append((line[0], line[1], line[3], line[4]))
    return vcf_dict 
printer = read_vcf(vcf_file)
print(printer)