import pandas as pd
import random


def merge_and_split_data_with_labels_save(
    tuesday_data,
    wednesday_data,
    ground_truth_tuesday,
    ground_truth_wednesday,
    num_parts=10,
    output_dir="./",
):
    random.shuffle(tuesday_data)
    random.shuffle(wednesday_data)

    parts_data = [[] for _ in range(num_parts)]
    parts_labels = [[] for _ in range(num_parts)]

    used_ids = set()
    part_index = 0

    for id, payload in tuesday_data:
        if id not in used_ids:
            label = ground_truth_tuesday.loc[
                ground_truth_tuesday["ID"] == id, "Label"
            ].values[0]
            parts_data[part_index].append((id, payload))
            parts_labels[part_index].append(label)
            used_ids.add(id)
            part_index = (part_index + 1) % num_parts

    for id, payload in wednesday_data:
        if id not in used_ids:
            label = ground_truth_wednesday.loc[
                ground_truth_wednesday["ID"] == id, "Label"
            ].values[0]
            parts_data[part_index].append((id, payload))
            parts_labels[part_index].append(label)
            used_ids.add(id)
            part_index = (part_index + 1) % num_parts

    total_lines = 0

    for i in range(num_parts):
        txt_filename = f"{output_dir}/part_{i + 1}.txt"
        with open(txt_filename, "w") as f:
            for id, payload in parts_data[i]:
                f.write(f"{id}; {payload}\n")
            total_lines += len(parts_data[i])

        csv_filename = f"{output_dir}/part_{i + 1}_ground_truth.csv"
        df = pd.DataFrame(
            {"ID": [id for id, _ in parts_data[i]], "Label": parts_labels[i]}
        )
        df.to_csv(csv_filename, index=False)

    print(f"Total number of lines across all parts: {total_lines}")


tuesday_file = "/home/apta/neuralnetwork-AD/rnn-apta/texts_cleaned/Tuesday-WorkingHours_testing_80.txt"
wednesday_file = "/home/apta/neuralnetwork-AD/rnn-apta/texts_cleaned/Wednesday-WorkingHours_testing_80.txt"
ground_truth_tuesday_file = (
    "/home/apta/CIC-IDS-2017/CSVs/TrafficLabelling/Tuesday-WorkingHours.pcap_ISCX.csv"
)
ground_truth_wednesday_file = (
    "/home/apta/CIC-IDS-2017/CSVs/TrafficLabelling/Wednesday-workingHours.pcap_ISCX.csv"
)

merge_and_split_data_with_labels_save(
    tuesday_file, wednesday_file, ground_truth_tuesday_file, ground_truth_wednesday_file
)
