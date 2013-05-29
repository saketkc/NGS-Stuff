from Bio import SeqIO
import sys
from itertools import islice
def get_format(seqio):
    nnuc = 50000
    start = 0
    skip = 4
    max_quality = 40
    min_seen = 128
    max_seen = 0
    nuc_count = 0
    seq_count = 0
    possible_encodings = set(('sanger', 'solexa', 'illumina'))
    possible_encodings = set(possible_encodings)
    sanger_min = 33
    solexa_min = 59
    illumina_min = 64
    solexa_threshold = solexa_min - sanger_min
    illumina_threshold = illumina_min - sanger_min
    seqio_slice = islice(seqio, start, None, skip + 1)
    for record in seqio_slice:
        seq_count += 1
        qualities = record.letter_annotations["phred_quality"]
        min_seen = min(min_seen, min(qualities))
        max_seen = max(max_seen, max(qualities))
        # Eliminate possibilities
        if 'sanger' in possible_encodings and max_seen > max_quality:
            possible_encodings.remove('sanger')
        if 'solexa' in possible_encodings and min_seen < solexa_threshold:
            return 'sanger'
        if 'illumina' in possible_encodings and min_seen < illumina_threshold:
            possible_encodings.remove('illumina')
        # Check if we finished early
        if len(possible_encodings) == 1:
            return possible_encodings.pop()
        elif len(possible_encodings) == 0:
            raise ValueError("Could not identify FASTQ file %s: eliminated all possible encodings." % (filename,))
        if nnuc:
            nuc_count += len(record)
            if nuc_count >nnuc:
                break
    # If no Illumina-encoded quality less than zero has been seen,
    # then eliminate solexa and return illumina.
    if min_seen >= illumina_threshold:
        return 'illumina'
    else:
        return 'solexa'


possible_encodings = set(("solexa", "sanger", "illumina"))
filename = sys.argv[1]
seqio = SeqIO.parse(filename, "fastq-sanger")
print get_format(seqio)
